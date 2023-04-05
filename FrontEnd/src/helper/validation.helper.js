class Helper {
  ValidationMessage = [];
  validationRegex = {
    name: /^[a-zA-Z]+(\s[a-zA-Z]+)?$/,
    pincode: /^[0-9]{6}$/,
    number: /^([+]\d{2})?\d{10}$/,
    email: /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/,
  };

  validationPincode = (pincode) => {
    // console.log("pincode",code)
    if (pincode.toString().match(this.validationRegex.pincode)) {    
      this.ValidationMessage["pincode"] = "";
    } else {
      this.ValidationMessage["pincode"] = "Please entered valid pincode";
    }
  };

  validationContactPersonName = (contactPersonName) => {
    if (contactPersonName.match(this.validationRegex.name)) {
      this.ValidationMessage["contactPersonName"] = "";
    } else {
      this.ValidationMessage["contactPersonName"] = "Please entered a valid name";
    }
  };

  validationNgoName = (ngoName) => {
    if (ngoName.match(this.validationRegex.name)) {
      this.ValidationMessage["ngoName"] = "";
    } else {
      this.ValidationMessage["ngoName"] = "Please entered a valid name";
    }
  };

  validationLocation = (location) => {
    if (location.match(this.validationRegex.name)) {
      this.ValidationMessage["location"] = "";
    } else {
      this.ValidationMessage["location"] = "Please entered a valid name";
    }
  };

  validationEmail = (contactPersonEmail) => {
    if (contactPersonEmail.match(this.validationRegex.email)) {
      this.ValidationMessage["email"] = "";
    } else {
      this.ValidationMessage["email"] = "Please entered a valid email";
    }
  };

  validationPhoneNumber = (contactPersonPhone) => {
    if (contactPersonPhone.toString().match(this.validationRegex.number)) {
      this.ValidationMessage["phoneNumber"] = "";
    } else {
      this.ValidationMessage["phoneNumber"] = "Please entered a valid phoneNumber";
    }
  };

  validationsOfAllfields = (newNgo) => {
    if (
      newNgo.contactPersonEmail.match(this.validationRegex.email) &&
      newNgo.contactPersonPhone.toString().match(this.validationRegex.number) &&
      newNgo.pincode.toString().match(this.validationRegex.pincode) &&
      newNgo.contactPersonName.match(this.validationRegex.name) &&
      newNgo.ngoName.match(this.validationRegex.name) &&
      newNgo.location.match(this.validationRegex.name)
    ) {
      return true;
    }
  };
}
export default new Helper();
