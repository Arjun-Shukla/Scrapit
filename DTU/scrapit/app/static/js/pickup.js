const body = document.querySelector("body");
const btns = document.querySelectorAll(".choices");

btns.forEach((val, idx) => {
  console.log(idx);
  console.log(val);
  let initialbgcolor = getComputedStyle(btns[idx]).background;
  val.addEventListener("click", () => {
    let currentbgcolor = getComputedStyle(btns[idx]).background;
    if (initialbgcolor === currentbgcolor) {
      console.log(idx);
      btns[idx].style.background =
        "linear-gradient(90deg, #57c785 0%, #b3cc6e 100%)";
      currentbgcolor = "linear-gradient(90deg, #57c785 0%, #b3cc6e 100%)";
      console.log(initialbgcolor);
      console.log(currentbgcolor);
    } else if (initialbgcolor !== currentbgcolor) {
      btns[idx].style.background = initialbgcolor;
    }
  });
});

const body2 = document.querySelector("body");
const btns2 = document.querySelectorAll(".slot-btn");

btns2.forEach((val2, idx2) => {
  console.log(idx2);
  console.log(val2);
  let initialbgcolor2 = getComputedStyle(btns2[idx2]).background;
  val2.addEventListener("click", () => {
    let currentbgcolor2 = getComputedStyle(btns2[idx2]).background;
    if (initialbgcolor2 === currentbgcolor2) {
      console.log(idx2);
      btns2[idx2].style.background =
        "linear-gradient(90deg, #57c785 0%, #b3cc6e 100%)";
      currentbgcolor2 = "linear-gradient(90deg, #57c785 0%, #b3cc6e 100%)";
      console.log(initialbgcolor2);
      console.log(currentbgcolor2);
    } else if (initialbgcolor2 !== currentbgcolor2) {
      btns2[idx2].style.background = initialbgcolor2;
    }
  });
});
