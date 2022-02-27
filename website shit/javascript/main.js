// Dark mode function button
function darkMode() {
 var element = document.body;
   element.classList.toggle("dark-mode");
 }

 // Decides the theme based on the users system preference
    const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

    if (prefersDarkScheme.matches) {
      document.body.classList.add("dark-mode");
    }
    else {
      document.body.classList.remove("dark-mode");
    }

    // Date feature
    n =  new Date();
    y = n.getFullYear();
    m = n.getMonth() + 1;
    d = n.getDate();
    document.getElementById("date").innerHTML = m + "/" + d + "/" + y;
