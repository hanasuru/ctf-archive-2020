var ind = 0;
var seq = ['RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'DOWN', 'ENTER', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'ENTER', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER', 'LEFT', 'ENTER', 'DOWN', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'ENTER', 'LEFT', 'LEFT', 'ENTER', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'UP', 'ENTER', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'ENTER', 'UP', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER', 'UP', 'UP', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'ENTER', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'ENTER', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER', 'UP', 'UP', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'ENTER', 'DOWN', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'DOWN', 'ENTER', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER', 'UP', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'ENTER', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'UP', 'ENTER', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'ENTER', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'ENTER'];
function solve(e) {
    k = document.getElementsByClassName("selected")[0];
    if (e == 'UP') {
        // up arrow
        row = parseInt(k.id.split('-')[0]);
        col = parseInt(k.id.split('-')[1]);

        // if top, do nothing
        if(row == 1) return;
        k.classList.remove('selected');
        row -= 1;
        col = col.toString().length <2 ? '0'+col:col;
        k = document.getElementById(row.toString()+'-'+col)
        k.classList.add('selected')
    }
    else if (e == 'DOWN') {
        // down arrow
        row = parseInt(k.id.split('-')[0]);
        col = parseInt(k.id.split('-')[1]);

        // if bottom, do nothing
        if(row == 3) return;
        k.classList.remove('selected');
        row += 1;
        if (row==3 && col==26) col = 25;
        col = col.toString().length <2 ? '0'+col:col;
        k = document.getElementById(row.toString()+'-'+col)
        k.classList.add('selected')
    }
    else if (e == 'LEFT') {
       // left arrow
       row = parseInt(k.id.split('-')[0]);
       col = parseInt(k.id.split('-')[1]);

       // if left, do nothing
       if(col == 1) return;
       k.classList.remove('selected');
       col -= 1;
       col = col.toString().length <2 ? '0'+col:col;
       k = document.getElementById(row.toString()+'-'+col)
       k.classList.add('selected')
    }
    else if (e == 'RIGHT') {
       // right arrow
       row = parseInt(k.id.split('-')[0]);
       col = parseInt(k.id.split('-')[1]);

       // if right, do nothing
       if(col == 26 || (row==3 && col == 25)) return;
       k.classList.remove('selected');
       col += 1;
       col = col.toString().length <2 ? '0'+col:col;
       k = document.getElementById(row.toString()+'-'+col)
       k.classList.add('selected')
    }
    else if(e == 'ENTER'){
    	val = k.innerText;
    	if(val != 'Del' && ind < 26){
    		flag[ind++] = val;
    		col = (ind).toString().length < 2? '0'+(ind).toString(): (ind).toString();
			f = document.getElementById('f-'+col);
			f.classList.add('filled');
    		f.innerText = val;
    	} else if(ind > 0 && val == 'Del'){
    		// del
    		flag[--ind] = ' ';
    		col = (ind+1).toString().length < 2? '0'+(ind+1).toString(): (ind+1).toString();
			f = document.getElementById('f-'+col);
			f.classList.remove('filled');
			f.innerText = ' ';
    	}
    }
}

for(var i=0;i<seq.length;i++){
  solve(seq[i])
}