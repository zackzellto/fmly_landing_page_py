import { Card } from "@material-ui/core";
import "../../Styles/PricingStructureStyles.css";
import {  CalendarDaysIcon, BellAlertIcon, ClipboardDocumentCheckIcon, GiftIcon, ChatBubbleBottomCenterTextIcon, MapPinIcon, BanknotesIcon  } from '@heroicons/react/24/solid'



const PremiumPricingModel = () => {
 
  return (
    <Card className="pricing-box-premium">
      <div className="pricing-box-premium-bg">
        <div className="pricing-box-premium-title">
          Premium      
            <div className="pricing-box-premium-price">
              <div className="pricing-box-premium-price-text">
                $9.99/mo.
                </div>
              </div>
      </div>


      
      </div>
      <div className="pricing-box-text-premium">
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

  <li className="pricing-box-text-free-li">
    <div className="flex items-center">
      <GiftIcon className="h-6 w-6 text-purple-500 mr-2"/>
      <div className="pricing-box-text-free-li-text">bountyboard</div>
    </div>    
  </li>
  <li className="pricing-box-text-free-li">
    <div className="flex items-center">
      <MapPinIcon className="h-6 w-6 text-blue-500 mr-2"/>
      <div className="pricing-box-text-free-li-text">Find My fmly</div>
    </div>    
  </li>
  <li className="pricing-box-text-free-li">
    <div className="flex items-center">
      <BanknotesIcon className="h-6 w-6 text-green-500 mr-2"/>
      <div className="pricing-box-text-free-li-text">Cash Quest!</div>
    </div>    
  </li>

</ol>
</div>
      </div>

    </Card>
  );
};

export default PremiumPricingModel;
