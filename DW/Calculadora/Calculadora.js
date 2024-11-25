const result= document.querySelector("#result");
const buttons= document.querySelectorAll("button");

buttons.forEach((btn) => {
    btn.addEventListener("click", () =>{
        if(btn.id === "="){
            result.value = eval(result.value);
        } else if (btn.id === "ac"){
            result.value = "";
        } else if (btn.id == "de"){
            result.value = result.value.slice(0, -1);
        } else {
            result.value += btn.id
        }
    })
})