class Helper {
  shownameError=false;
  msg={
    name:"",
    pincode:"",
    number:"",
    email:""
  };
  validationRegex = {
    name: /^[a-zA-Z]+(\s[a-zA-Z]+)?$/,
    pincode: /^[0-9]{6}$/,
    number: /^([+]\d{2})?\d{10}$/,
    email: /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/,
  };

  validatePincode = (pincode) =>
    pincode.toString().match(this.validationRegex.pincode)
      ? ""
      : "Please entered valid code";
  
  validateName = (e) =>{
    // debugger
    const name = e.target.value;
    console.log("nameee",name,name.match(this.validationRegex.name))
    if(!name.match(this.validationRegex.name)){
    console.log("22222222222")
      this.shownameError=true;
      this.msg.name= "Please entered a valid name";
    }
    else{
      console.log("validatioErr")
      this.shownameError=true
      this.msg.name="";
    }
  }
  validateEmail = (contactPersonEmail) =>
    contactPersonEmail.match(this.validationRegex.email)
      ? ""
      : "Please entered a valid email";

  validatePhoneNumber = (contactPersonPhone) =>
    contactPersonPhone.toString().match(this.validationRegex.number)
      ? ""
      : "Please entered a valid phoneNumber";

  isErrorMessagesAvailable = (obj) => {
    console.log("obj",obj);
    var isError = false;
    for (const key in obj) {
      if (obj[key] !== "") {
        isError = true;
        break;
      }
    }
    return isError;
  };
  
  validateDateRange = (fromDate,toDate)=> 
    fromDate && toDate?
    new Date(fromDate) >= new Date(toDate) ? 'From date must be earlier than to date':"":"Please a Enter a Date"
  
}
export default new Helper();
