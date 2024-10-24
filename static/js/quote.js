function sendMail() {
    alert("Your message!!");
    var params = {
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      details: document.getElementById("phone").value,
      email: document.getElementById("serviceType").value,
      details: document.getElementById("details").value,
    };
  
    const serviceID = "service_6zbbn5d";
    const templateID = "template_4jv30in";
  
      emailjs.send(serviceID, templateID, params)
      .then(res=>{
          document.getElementById("name").value = "";
          document.getElementById("email").value = "";
          document.getElementById("phone").value = "";
          document.getElementById("serviceType").value = "";
          document.getElementById("details").value = "";
          console.log(res);
          alert("Your message sent successfully!!")
  
      })
      .catch(err=>console.log(err));
  
  }