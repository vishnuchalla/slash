import React , {useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import { TextField, Button, Container, Table, TableBody, TableCell, TableRow, TableHead} from '@material-ui/core';
import SearchIcon from '@material-ui/icons/Search';

const useStyles = makeStyles((theme) => ({
    head: {
        backgroundColor: theme.palette.primary.main,
        color: theme.palette.common.white,
        fontSize: 14,
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
  const [users, setUsers] = useState([])
  const classes = useStyles();
  const paperStyle ={padding:'50px 40px', width:400, margin:'155px auto'}

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
   //console.log(data)
        console.log("Search is sent to back end")
      }
}


  return (
    <div>
    <Container>
    <Paper elevation={3} style={paperStyle}>
    <h1 style={{color:'blue'}}>Sla$h</h1>
    <form className={classes.root} noValidate autoComplete="off">
    <TextField id="outlined-basic" label="Search product here" variant="outlined" value={search} onChange={(e)=>setToSearch(e.target.value)} required="required" fullWidth/><br/><br/>
    <TextField id="outlined-basic" label="No of results to be displayed" type="number" variant="outlined" value={num} onChange={(e)=>setNumb(e.target.value)} required="required" min="3" fullWidth/><br/><br/>
    <TextField id="outlined-basic" label="Enter Email Id" variant="outlined" value={email} onChange={(e)=>setEmail(e.target.value)}  fullWidth/>{error && <h4 style={{color: 'red'}}>{error}</h4>}<br/><br/>
    <Button variant="contained" color="primary" size="large" className={classes.button} onClick={handleClick}>Search <SearchIcon/></Button>
    </form>
    </Paper>
    </Container>
    <h1 style={{color:'blue'}}>Here are your results :)</h1>
    <Container>
    <Paper elevation={3} className={classes.root}>
      <Table className={classes.table}>
        <TableHead className={classes.head}>
          <TableRow>
            <TableCell align="right">Title</TableCell>
            <TableCell align="right">Website</TableCell>
            <TableCell align="right">Price</TableCell>
            <TableCell align="right">Rating</TableCell>
            <TableCell align="right">Timestamp</TableCell>
            <TableCell>Where to find?</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {users.map(user => (
            <TableRow>
              <TableCell component="th" scope="row">
                {user.link}
              </TableCell>
              <TableCell align="right">{user.price}</TableCell>
              <TableCell align="right">{user.rating}</TableCell>
              <TableCell align="right">{user.timestamp}</TableCell>
              <TableCell align="right">{user.title}</TableCell>
              <TableCell align="right">{user.website}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Paper>
    </Container>
    </div>
  );
}
