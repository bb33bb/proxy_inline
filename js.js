if (document.location.pathname == '/search'){
    nodes=["gb_36", "gb_8", "gb_78", "gb_23", 'gb_49', 'gb_119', 'gbg', 'gbztms', 'pushdown', 'fbarcnt'];
}
else{
    document.getElementById("lga").style.marginTop=0;
    nodes=["prm-pt", "footer", "mngb", 'pushdown'];
    document.getElementById('hplogo').getElementsByTagName('div')[0].innerHTML='疯狂的小企鹅<a style="display:block; color:#ccc;font-size:14px;padding-top:25px;" target="_blank" href="http://www.tuxpy.info/page/dQs6SNSuSB6dArlDpwqJPruAomKZvkb/v1scAZkIIg4=">使用手册</a>';
    document.getElementById('lst-ib').focus()
}

for (var i=0;i<nodes.length;i++){
    c=document.getElementById(nodes[i]);
    if (c == null)continue;
    c.parentNode.removeChild(c);
}
setTimeout("window.stop()", 2000);
