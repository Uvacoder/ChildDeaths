#Child Deaths
- Ran <a href="http://www.myajc.com/child-deaths/" target="_blank">here</a> on 3/9/13 in conjunction with <a href="http://www.myajc.com/news/news/once-a-national-model-georgias-child-death-reviews/nd7ZC/" target="_blank">this</a> story.
- Uses <a href="http://getbootstrap.com/" target="_blank">Bootstrap</a> and <a href="https://github.com/Mottie/tablesorter" target="_blank">this fork of TableSorter</a>

##To update
- Run spreadsheets through corresponding Python scripts to create JSON particular to TableSorter's Build Table widget

###To do
- Table is NOT responsive enough - cols will not collapse enough to fit everything (even 4 col table) inside the viewport, which causes bootstrap piece to size incorrectly because the table is forcing the page to be wider than the viewport on mobile Safari (fine on desktop browsers)- TableSorter was kinda a pain, look in to using <a href="https://github.com/DataTables/DataTables" target="_blank">DataTables</a> instead
