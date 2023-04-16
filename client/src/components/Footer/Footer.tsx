import Grid from "@mui/material/Unstable_Grid2";
import './FooterStyles.css'

type Props = {}

const sendEmail = () => {
  window.location.href = `mailto:${process.env.EMAIL_ME}`
}


const Footer = (props: Props) => {
  return (
    <div>
      <h3 style={{color: "black", width: "52%", marginTop: "70px", margin: "auto"}} >fmly is in development. Designs, features, and other functions of the app may change.
        As a solo developer, I will provide updates to everyone who signs up for the waitlist throw new 
        keep everyone updated with the status of the app. <br /> Thank you to everyone who has signed up
        and I can't wait for everyone to start using fmly!
        
      </h3>
      <Grid>
        <ol style={{marginTop: "40px"}}>
          <li className="footer-li">
            About
          </li>
          <li className="footer-li">
            <a onClick={sendEmail}>
            Contact
            </a>
          </li>
        </ol>
        </Grid>
        </div>
  )
}

export default Footer