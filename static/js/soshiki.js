/**
 * Created by jeanmoongill on 2017. 4. 1..
 */

$(document).ready(function () {
   $('#soshiki').DataTable({
       ordering: true,
       searching: false,
       "language": {
            "sProcessing":   "処理中...",
            "sLengthMenu":   "",
            "sZeroRecords":  "データはありません。",
            "sInfo":         " _END_/_TOTAL_ 件",
            "sInfoEmpty":    " 0 件中 0 から 0 まで表示",
            "sInfoFiltered": "（全 _MAX_ 件より抽出）",
            "sInfoPostFix":  "",
            "sSearch":       "検索:",
            "sUrl":          "",
            "oPaginate": {
                "sFirst":    "先頭",
                "sPrevious": "前",
                "sNext":     "次",
                "sLast":     "最終"
            }
       }
   });
});
