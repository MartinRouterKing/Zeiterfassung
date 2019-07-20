
     function ajax_exp() {
        var table = document.getElementsByTagName("table")[0];
        var data = [];

        for (var c = 0; c< table.rows.length; c++) {
            console.log(c);
            rows = []
            for (var i = 0; i< table.rows[0].cells.length; i++) {
                if (c == 0){
                   rows.push(table.rows[c].cells[i].innerText);
                } else {
                   rows.push(table.rows[c].cells[i].innerHTML);
                }
            };
            data.push(rows);
        };

        let csvContent = "data:text/csv;charset=UTF-8,";
        data.forEach(function(rowArray){
        let row = rowArray.join(",");
        csvContent += row + "\r\n";
        });

        var encodedUri = encodeURI(csvContent);
        var encodedUri = encodeURI(csvContent);
        var link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", "my_data.csv");
        document.body.appendChild(link); // Required for FF
        link.click(); // This will download the data file named "my_data.csv".
     };
