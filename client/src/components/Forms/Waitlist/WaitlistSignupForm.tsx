import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Axios from "axios";
import Grid from "@mui/material/Unstable_Grid2";
import { validateEmail } from "../FormValidationChecker";
import "./WaitlistSignup.css";
import WaitlistAlert from "../../../components/Alerts/WaitlistAlert";
import axios from "axios";


export const WaitlistSignupForm = () => {

  const [email, setEmail] = useState('');
  const [showAlert, setShowAlert] = useState(false);


  const checkEmail = () => {
    if (validateEmail(email)) {
      return true;
    } else {
      return false;
    }
  };

  const handleSubmit = async (event : any) => {
    event.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/api/waitlist", {
        email: email,
      });
      console.log(response.data);
      // add code to handle successful response from API
    } catch (error) {
      console.error(error);
      // add code to handle error from API
    }
  };
  

  return (
    <>
      <form className="wl-input-form" noValidate autoComplete="off">
        <div>
          <Grid container spacing={2}>
            <Grid xs={12} md={6}>
              <div className="wl-spacer"></div>
              <TextField
                className="wl-input"
                id="outlined-email-input"
                label="Email"
                type="email"
                variant="outlined"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
              <div className="wl-spacer"></div>
              <Button
              style={{ 
              backgroundColor: "#83F3DF", 
              color: "black", 
              fontWeight: "bold", 
              fontSize: "16px", 
              fontFamily: "Poppins, sans-serif",
              borderRadius: "10px", 
              padding: "10px 20px", 
              cursor: "pointer",
              border: "1px solid #83F3DF",
              boxShadow: "0px 3px 3px rgba(0, 0, 0, 0.25)",
              transition: "all 0.2s ease-in-out",
               }}
                className="wl-button"
                type="submit"  
                onClick={handleSubmit}
              >
                Join Waitlist!
              </Button>
            </Grid>
          </Grid>
        </div>
      </form>
    </>
  );
};
