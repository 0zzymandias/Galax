//Import libraries.

console.log("Yo yo yo!")

console.log("Normal %cStyled %clorem %cipsum", "color: blue; font-weight: bold", "color: red", "background-image: linear-gradient(red, blue); color: white; padding: 5px;")

function adder(x,y) {
    z = x+y
}

adder(1,3)
console.log(z)

function interest(x,y,z) {
    interest = x+y+z
    //x = principle, y = interest rate, z = periods of time
}
interest(10,0.01,10)
console.log(interest)
//Prints 20.00999 -- floating point precision

var i = 0
while (i<=100) {
    console.log(i)
    i+=1
}

document.write("Normal %cStyled %clorem %cipsum", "color: blue; font-weight: bold", "color: red", "background-image: linear-gradient(red, blue); color: white; padding: 5px;")