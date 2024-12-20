// cài đặt mặc định
document.getElementById("showcart").style.display = "none";

var giohang = new Array();

function themvaogiohang(x) {
    var boxsp = x.parentElement.children;
    var hinh = boxsp[0].children[0].src;
    var gia = boxsp[1].children[0].innerText;
    var tensp = boxsp[2].innerText;
    var soluong = parseInt(boxsp[3].value);
    var sp = new Array(hinh, gia, tensp, soluong);

    // kiểm tra trong giỏ hàng
    var kt = 0;
    for (let i = 0; i < giohang.length; i++) {
        if (giohang[i][2] == tensp) {
            kt = 1;
            soluong += parseInt(giohang[i][3]);
            giohang[i][3] = soluong;
            break;
        }

    }
    if (kt == 0) {
        //thêm mới - add to cart
        giohang.push(sp);
    }


    // console.log(giohang);
    showcountsp();

    // lưu giỏ hàng lên session storage
    sessionStorage.setItem("giohang", JSON.stringify(giohang));
}

function showcountsp() {
    document.getElementById("countsp").innerHTML = giohang.length;
}

function showmycart() {
    var ttgh = "";
    var tong = 0;
    for (let i = 0; i < giohang.length; i++) {
        var tt = parseInt(giohang[i][1]) * parseInt(giohang[i][3]);
        tong += tt;
        ttgh += '<tr>' +
            '<td>' + (i + 1) + '</td>' +
            '<td><img src="' + giohang[i][0] + '" alt=""></td>' +
            '<td>' + giohang[i][2] + '</td>' +
            '<td>' + giohang[i][1] + '</td>' +
            '<td>' + giohang[i][3] + '</td>' +
            '<td>' +
            '<div>' + tt + '</div>' +
            '</td>' +
            '<td>' +
            '<button onclick = "xoasp(this)">Xóa</button>' +
            '</td>' +
            '</tr>';
    }
    ttgh += '<tr>' +
        '<th colspan="6">Tổng đơn hàng</th>' +
        '<th>' +
        '<div>' + tong + '</div>' +
        '</th>' +
        '</tr>';

    document.getElementById("mycart").innerHTML = ttgh;
}

function xoasp(x) {
    // xóa tr
    var tr = x.parentElement.parentElement;
    var tensp = tr.children[2].innerText;
    tr.remove();
    // alert(tensp);

    // xóa sản phẩm trong mảng
    for (let i = 0; i < giohang.length; i++) {
        if (giohang[i][2] == tensp) {
            giohang.splice(i, 1);

        }
    }
    //console.log(giohang);
    showmycart();
    showcountsp();
}

function xoatatca() {
    giohang = [];
    showmycart();
    showcountsp();
}

function showcart() {

    var x = document.getElementById("showcart");
    if (x.style.display == "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
        showmycart();
    }

}

function showgiohang_trangthanhtoan() {
    var gh = sessionStorage.getItem("giohang");
    var giohang = JSON.parse(gh);
    var ttgh = "";
    var tong = 0;
    for (let i = 0; i < giohang.length; i++) {
        var tt = parseInt(giohang[i][1]) * parseInt(giohang[i][3]);
        tong += tt;
        ttgh += '<tr>' +
            '<td>' + (i + 1) + '</td>' +
            '<td><img src="' + giohang[i][0] + '" alt=""></td>' +
            '<td>' + giohang[i][2] + '</td>' +
            '<td>' + giohang[i][1] + '</td>' +
            '<td>' + giohang[i][3] + '</td>' +
            '<td>' +
            '<div>' + tt + '</div>' +
            '</td>' +
            '</tr>';
    }
    ttgh += '<tr>' +
        '<th colspan="5">Tổng đơn hàng</th>' +
        '<th>' +
        '<div>' + tong + '</div>' +
        '</th>' +
        '</tr>';

    document.getElementById("mycart").innerHTML = ttgh;
}

function dongydathang() {
    var ttnh = document.getElementById("thongtinnhanhang").children;
    var hoten = ttnh[0].children[1].children[0].value;
    var diachi = ttnh[1].children[1].children[0].value;
    var dienthoai = ttnh[2].children[1].children[0].value;
    var email = ttnh[3].children[1].children[0].value;

    var nguoinhan = new Array(hoten, diachi, dienthoai, email);
    console.log(nguoinhan);
    sessionStorage.setItem("nguoinhan", JSON.stringify(nguoinhan));

    window.location.assign("donhang.html");

}

function showthongtinnguoinhan() {
    var nguoinhan = sessionStorage.getItem("nguoinhan");
    var thongtin = JSON.parse(nguoinhan);

    var tt = '<tr>' +
        '<td width="20%">Họ tên</td>' +
        '<td>' + thongtin[0] + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Địa chỉ</td>' +
        '<td>' + thongtin[1] + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Điện thoại</td>' +
        '<td>' + thongtin[2] + '</td>' +
        '</tr>' +
        '<tr>' +
        '<td>Email</td>' +
        '<td>' + thongtin[3] + '</td>' +
        '</tr>';

    document.getElementById("thongtinnhanhang").innerHTML = tt;
}