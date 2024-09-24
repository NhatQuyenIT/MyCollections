function addBorrowRow() {
    const table = document.getElementById('borrow-table').getElementsByTagName('tbody')[0];
    const rowCount = table.rows.length;
    const row = table.insertRow(rowCount);
    const cells = ['STT', 'Mã Sách', 'Tên Sách', 'Ngày mượn', 'Ngày trả'];

    cells.forEach((cell, index) => {
        const newCell = row.insertCell(index);
        if (index === 0) {
            newCell.innerHTML = rowCount + 1;
        } else {
            const input = document.createElement('input');
            input.type = 'text';
            input.name = cell.toLowerCase().replace(' ', '-');
            newCell.appendChild(input);
        }
    });
}

function addImportRow() {
    const table = document.getElementById('import-table').getElementsByTagName('tbody')[0];
    const rowCount = table.rows.length;
    const row = table.insertRow(rowCount);
    const cells = ['STT', 'Mã Sách', 'Tên Sách', 'Tác giả', 'Thể loại', 'Ngày Nhập'];

    cells.forEach((cell, index) => {
        const newCell = row.insertCell(index);
        if (index === 0) {
            newCell.innerHTML = rowCount + 1;
        } else {
            const input = document.createElement('input');
            input.type = 'text';
            input.name = cell.toLowerCase().replace(' ', '-');
            newCell.appendChild(input);
        }
    });
}

function locMuonSachTheoKhoangNgay() {
    const fromDate = document.getElementById('fromDate1').value;
    const toDate = document.getElementById('toDate1').value;

    if (!fromDate || !toDate) {
        alert("Vui lòng chọn khoảng ngày hợp lệ.");
        return;
    }

    const table = document.getElementById('borrow-table').getElementsByTagName('tbody')[0];
    const rows = table.rows;
    
    for (let i = 0; i < rows.length; i++) {
        const ngayMuon = rows[i].cells[3].children[0].value;
        if (ngayMuon >= fromDate && ngayMuon <= toDate) {
            rows[i].style.display = '';
        } else {
            rows[i].style.display = 'none';
        }
    }
}

function locNhapSachTheoKhoangNgay() {
    const fromDate = document.getElementById('fromDate2').value;
    const toDate = document.getElementById('toDate2').value;

    if (!fromDate || !toDate) {
        alert("Vui lòng chọn khoảng ngày hợp lệ.");
        return;
    }

    const table = document.getElementById('import-table').getElementsByTagName('tbody')[0];
    const rows = table.rows;
    
    for (let i = 0; i < rows.length; i++) {
        const ngayNhap = rows[i].cells[5].children[0].value;
        if (ngayNhap >= fromDate && ngayNhap <= toDate) {
            rows[i].style.display = '';
        } else {
            rows[i].style.display = 'none';
        }
    }
}
