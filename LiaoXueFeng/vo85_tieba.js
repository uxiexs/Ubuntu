Date.prototype.pattern=function(fmt) {
     var o = {
     "M+" : this.getMonth()+1, //月份
     "d+" : this.getDate(), //日
     //"h+" : this.getHours()%12 == 0 ? 12 : this.getHours()%12, //12小时制
     "h+" : this.getHours(), //24小时制
     "H+" : this.getHours(), //小时
     "m+" : this.getMinutes(), //分
     "s+" : this.getSeconds(), //秒
     "S" : this.getMilliseconds() //毫秒
     };
    var week = {
     "0" : "天",
     "1" : "一",
     "2" : "二",
     "3" : "三",
     "4" : "四",
     "5" : "五",
     "6" : "六"
     };
     if(/(y+)/.test(fmt)){
         fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
     }
     if(/(E+)/.test(fmt)){
       fmt=fmt.replace(RegExp.$1, ((RegExp.$1.length>1) ? (RegExp.$1.length>2 ? "星期" : "周") : "")+week[this.getDay()+""]);
     }
     for(var k in o){
         if(new RegExp("("+ k +")").test(fmt)){
             fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
         }
     }
     return fmt;
}

var date =new Date().pattern("挽尊于yyyy年MM月dd日  EEE hh时mm分ss秒S毫秒");

'<img changedsize="true" pic_type="0" class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=5effaaa52a2eb938ec6d7afae56385fe/4f4f3834349b033b51ad559e10ce36d3d539bd36.jpg" height="10" width="560">'+"<font color=#E10602/font><strong>"+" <br>—— "+date+"<br>—— 来自于萌萌的Ubuntu 16.04 LTS"+'<img class="BDE_Image" src="http://imgsrc.baidu.com/forum/w%3D580/sign=95d008c85de736d158138c00ab514ffc/937aa6efce1b9d16d024dc75fadeb48f8d54647b.jpg"height="25" width="25"></img> '+"& Chrome 54.0.2840.100 (64-bit)"+'<img class="BDE_Image" src="http://e.picphotos.baidu.com/album/s%3D1100%3Bq%3D90/sign=b3ad66d0a8345982c18ae1933cc40adc/d01373f082025aaf807f8c6ffeedab64024f1ac0.jpg"height="30" width="30">'+"<br><br>—— 鸣神の　少しとよみて　さし昙り　雨も降らんか　君を留めん"
