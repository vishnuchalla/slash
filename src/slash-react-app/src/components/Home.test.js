import React from "react";
import { render, waitFor, screen } from "@testing-library/react";
import Home, {isValidEmail} from "./Home";
import userEvent from "@testing-library/user-event";

//describe('email',() => {
  //  test('valid email function should pass on correct input', () =>{
    //    const text = "text@test.com";
      //  expect(isValidEmail(text)).toBe(true);
    //});
//});

describe('Form', ( )=> {
    const onClick = jest.fn();

    beforeEach(()=>{
        onClick.mockClear();
        render(<Home/>);
    });

    it("title validation",()=>{
        const title = screen.getByRole('textbox', {
            name: /enter email id/i
          })
    });

    it("number and spin button validation",()=>{
        const number = screen.getByRole('spinbutton',/no of results to be displayed/i)
    });

    it("email validation",()=>{
        const email = screen.getByRole('textbox', {
            name: /enter email id/i
          })
        });

    it("search button validation",()=>{
        const button = screen.getByRole('button',/search/i)
    });

    //users.click(screen.getByRole('button',{name: 'search'}));

});