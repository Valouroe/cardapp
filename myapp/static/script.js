var button=document.getElementById("but");
var d=document.getElementById("bl");
// d.className="";
var x=document.getElementById("e");
var numMessages=0;
// var check=0;
var obj="object";


// var div=document.createElement("div");
// d.classList.add("object");
button.addEventListener("click",display);
    function display(){
        console.log(window.check);
        numMessages++;
        var mess=document.getElementById("message").value;
        var na=document.getElementById("name").value;
        var para=document.createElement("p");
        var pa=document.createElement("p");
        var line=document.createElement("hr");
        var text=document.createTextNode(mess);
        var te=document.createTextNode(na);
        para.appendChild(text);
        pa.appendChild(te);
        pa.style["textAlign"]="right";
        pa.style["color"]="black";
        console.log(para);
        console.log(pa)
        d.appendChild(para);
        d.appendChild(pa);
        d.appendChild(line);
        // document.body.appendChild(d);
    
        // document.getElementById("bl").appendChild(para);
        // document.getElementById("bl").appendChild(pa);
        // document.getElementById("bl").appendChild(line);
    
        const rec=para.getBoundingClientRect();
        console.log(rec);
        diff=window.check*550;
        // document.getElementById("message").value="";
        // document.getElementById("name").value="";
        $(function() {
            if((rec.top-diff)>=550 ){
                console.log("k");
                console.log(diff);
                console.log(rec.top-diff);
                // $('.object').hide(1000);
                // $('object').show(1000);
                d=document.createElement("div");
                obj="object";
                d.classList.add(obj);
                window.check++;
                d.appendChild(para);
                d.appendChild(pa);
                d.appendChild(line);
                document.body.appendChild(d);
                
            }
            
        });
    }
var b=document.getElementById("button");
b.addEventListener("click",p)
function p(){
    window.print();
}
// else if(check==2 && rec.top>=550){
            //     $('.'+obj).hide(1000);
            //     div=document.createElement("div");
            //     obj="object"+check;
            //     div.classList.add(obj);
            //     check++;
            //     div.appendChild(para);
            //     div.appendChild(pa);
            //     div.appendChild(line);
            //     document.body.appendChild(div);
            // }
        //     // if(numMessages==2){
        //     //     check++;
        //     //     $('#'+obj).hide(1000);
        //     //     obj="object"+check;
        //     //     $('#'+obj).show(1000);
        //     //     numMessages=0;
        //     // }

