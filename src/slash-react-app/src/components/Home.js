import React , {useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import {TextField, Button, Container, Table, TableBody, TableCell, TableRow, TableHead} from '@material-ui/core';
import SearchIcon from '@material-ui/icons/Search';

const useStyles = makeStyles((theme) => ({
    head: {
        backgroundColor: '#3f51b5',
        color: 'white',
      },
  root: {
    margin: theme.spacing(1),
    width: '100%',
    //marginTop: theme.spacing.unit * 3,
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
  
  row: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.background.default,
    },
  },

  }));

export default function Home() {
  const[search,setToSearch]=useState('');
  const[num,setNumb]=useState('');
  const[email,setEmail]=useState('');
  const [error, setError] = useState(null);
  const [fetchData, setFetchData] = useState(null);
  const [users, setUsers] = useState([])
  const classes = useStyles();
  const paperStyle ={padding:'50px 40px', width:400, margin:'155px auto'}

  const validate = () => {
    return search.length &&  num.length;
  };

  function isValidEmail(email) {
    if(email==='')
    return ''
    else
    return /^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i.test(email);
  }
  const handleClick=(e)=>{
    e.preventDefault()
        if (!isValidEmail(email) && email!=='') {
        setError('Invalid Email');
        console.log("exiting invalid email");
        } else {
        setError(null);
        console.log("printing search");
        const searcher={search,num,email}
        console.log(searcher)
        const myurl  = `https://slash-app.herokuapp.com/slash?search=${search}&num=${num}&email=${email}`
        console.log(myurl)
        fetch(myurl)
   .then(response => response.json())
   .then(data => setUsers(data));
   const x=(data=>setUsers(data));
   if(x===''){
   setFetchData('Unable to fetch data');
      }
        console.log(email)

        if((data=>setUsers(data)!=='') && email!==''){
          alert("Email sent!");
        }
        console.log("Search is sent to back end")
      }
}


  return (
    <div>
    <Container>
    <Paper elevation={3} style={paperStyle}>
    <img alt=""
                src="logo.png"
                width="150"
                style={{ marginRight: "1.5em"}}
              /><br></br>
    <form className={classes.root} noValidate autoComplete="off">
    {fetchData && <h4 style={{color: 'red'}}>{fetchData}</h4>}
    <TextField id="outlined-basic" label="Search product here" name="title" variant="outlined" value={search} required onChange={(e)=>setToSearch(e.target.value)} fullWidth/><br/><br/>
    <TextField id="outlined-basic" type='number' label="No of results to be displayed" name="number" variant="outlined" value={num} required onChange={(e)=>setNumb(e.target.value)} InputProps={{ inputProps: { min: 3, max: 20 } }} precision={ 0 } fullWidth/><br/><br/>
    <TextField id="outlined-basic" label="Enter Email Id" name="email" variant="outlined" value={email} onChange={(e)=>setEmail(e.target.value)}  fullWidth/>{error && <h4 style={{color: 'red'}}>{error}</h4>}<br/><br/>
    <Button variant="contained" color="primary" size="large" className={classes.button} onClick={handleClick} disabled={!validate()}>Search <SearchIcon/></Button>
    </form>
    </Paper>
    </Container>
    <h1 style={{color:'#3f51b5'}}>Here are your results :)</h1>
    <Container>
    <Paper elevation={3} className={classes.root}>
      <Table className={classes.table}>
        <TableHead className={classes.head}>
          <TableRow>
            <TableCell style={{color:'#ffffff', fontSize: 17}} align="center">Title</TableCell>
            <TableCell style={{color:'#ffffff', fontSize: 17}} align="center">Website</TableCell>
            <TableCell style={{color:'#ffffff', fontSize: 17}} align="center">Price</TableCell>
            <TableCell style={{color:'#ffffff', fontSize: 17}} align="center">Rating</TableCell>
            <TableCell style={{color:'#ffffff', fontSize: 17}} align="center">Timestamp</TableCell>
            <TableCell style={{color:'#ffffff', fontSize: 17}} align="center">Link</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {users.map(user => (
            <TableRow>
              <TableCell component="th" scope="row">{user.title}</TableCell>
              <TableCell align="center">{user.website}</TableCell>
              <TableCell align="center">{user.price}</TableCell>
              <TableCell align="center">{user.rating}</TableCell>
              <TableCell align="center">{user.timestamp}</TableCell>
              <TableCell align="center">{user.link}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
    </Container>
    </div>
  );
}
