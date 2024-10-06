
var ans = {};

function check(values)
{  
    var split = values.split(' ');
    if (split[1] == split[2])
    {
        ans[split[0]] = 't';
    }
    else
        ans[split[0]] = 'f';

    var a=[];
    for (i in ans)
        a.push(ans[i]);
    document.getElementById('answerid').value = a;
}

// function answer()
// {
   
//     //a.substr(1,(a.length)-2);
//     document.getElementById('answerid').value = 'welcome';
// }
