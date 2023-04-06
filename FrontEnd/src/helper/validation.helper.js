class Helper {
  validationRegex = {
    name: /^[a-zA-Z]+(\s[a-zA-Z]+)?$/,
    pincode: /^[0-9]{6}$/,
    number: /^([+]\d{2})?\d{10}$/,
    email: /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/,
  };

  validatePincode = (pincode) =>
    pincode.toString().match(this.validationRegex.pincode)
      ? ""
      : "Please entered valid pincode";
  
  validateName = (contactPersonName) =>
    contactPersonName.match(this.validationRegex.name)
      ? ""
      : "Please entered a valid name";

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
}
export default new Helper();
