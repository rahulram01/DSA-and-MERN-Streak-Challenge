const info = [
  { firstname: "Rahul", secondname: "Ram", initial: "P" },
  { firstname: "Leo", secondname: "Messi", initial: "K" },
  { firstname: "John", secondname: "Tunik", initial: "K" },
  { firstname: "Yrat", secondname: "Kohli", initial: "R" },
];

const fullNameArr = info.map((user) => user.firstname + " " + user.secondname);
console.log(fullNameArr);

const counting = info.reduce((acc, curr) => {
  if (acc[curr.initial]) {
    acc[curr.initial] = ++acc[curr.initial];
  } else {
    acc[curr.initial] = 1;
  }
  return acc;
}, {});

console.log(counting);

const filtering = info.filter((x) => info.initial("K").map((x) => x.firstname));
console.log(filtering);
