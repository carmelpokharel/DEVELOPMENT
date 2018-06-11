
function testit() {
        var prog = editor.getDoc().getValue().concat('\nprint reverse("Carmel")');
        var mypre = document.getElementById("dynamicframe");
        window.alert(prog);
        mypre.innerHTML = '<b>RESULTS</b>:\n';
        Sk.pre = "dynamicframe";
        Sk.configure({
            output: outf,
            read: builtinRead
        });
        var myPromise = Sk.misceval.asyncToPromise(function() {
            return Sk.importMainWithBody("<stdin>", false, prog, true);
        });
        myPromise.then(function(mod) {
                console.log('success');
            },
            function(err) {
                console.log(err.toString());
            });
    }