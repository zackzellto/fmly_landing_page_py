import * as React from "react";
import {  CalendarDaysIcon, BellAlertIcon, ClipboardDocumentCheckIcon, GiftIcon, ChatBubbleBottomCenterTextIcon, MapPinIcon, BanknotesIcon  } from '@heroicons/react/24/solid'
import { Card, Grid } from "@material-ui/core";
import "../../Styles/PricingStructureStyles.css";

const FreePricingModel = () => {


  return (
    <Card className="pricing-box-free">
      <div className="pricing-box-free-bg">
      <div className="pricing-box-free-title">
        Free
      </div>
      

      
      </div>
      <div className="pricing-box-text-free">
        <div className="included-features" >Included Features</div>
        <div className="included-features-container">
        <ol>
  <li className="pricing-box-text-free-li">
    <div className="flex items-center">
      <CalendarDaysIcon className="h-6 w-6 text-red-500 mr-2"/>
      <div className="pricing-box-text-free-li-text">Calendar</div>
    </div>    
  </li>
  <li className="pricing-box-text-free-li">
    <div className="flex items-center">
      <ChatBubbleBottomCenterTextIcon className="h-6 w-6 text-blue-500 mr-2"/>
      <div className="pricing-box-text-free-li-text">fmlyChat</div>
    </div>    
  </li>
  <li className="pricing-box-text-free-li">
    <div className="flex items-center">
      <BellAlertIcon className="h-6 w-6 text-yellow-500 mr-2"/>
      <div className="pricing-box-text-free-li-text">Dinnertime!</div>
    </div>    
  </li>
  <li className="pricing-box-text-free-li">
    <div className="flex items-center">
      <BanknotesIcon className="h-6 w-6 text-green-500 mr-2"/>
      <div className="pricing-box-text-free-li-text">Groceries</div>
    </div>    
  </li>
  <li className="pricing-box-text-free-li">
    <div className="flex items-center">
      <ClipboardDocumentCheckIcon className="h-6 w-6 text-orange-500 mr-2"/>
      <div className="pricing-box-text-free-li-text">To-Do List</div>
    </div>    
  </li>
</ol>
</div>

      </div>

    </Card>
  );
};

export default FreePricingModel;
