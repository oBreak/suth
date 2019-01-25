#JS

    eval(function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[c.toString(a)]=k[c]||c.toString(a)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('1 i(4){h 8={"4":4};$.9({a:"7",5:"6",g:8,b:\'/d/e/n\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}1 j(){$.9({a:"7",5:"6",b:\'/d/e/k/l/m\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}',24,24,'response|function|log|console|code|dataType|json|POST|formData|ajax|type|url|success|api|invite|error|data|var|verifyInviteCode|makeInviteCode|how|to|generate|verify'.split('|'),0,{}))

## Breaking it down

    eval(function(p, a, c, k, e, d) {
        e = function(c) {
            return c.toString(36)
        };
        if (!''.replace(/^/, String)) {
            while (c--) {
                d[c.toString(a)] = k[c] || c.toString(a)
            }
            k = [function(e) {
                return d[e]
            }];
            e = function() {
                return '\\w+'
            };
            c = 1
        };
        while (c--) {
            if (k[c]) {
                p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c])
            }
        }
        return p
    }('1 i(4){h 8={"4":4};$.9({a:"7",5:"6",g:8,b:\'/d/e/n\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}1 j(){$.9({a:"7",5:"6",b:\'/d/e/k/l/m\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}', 24, 24, 'response|function|log|console|code|dataType|json|POST|formData|ajax|type|url|success|api|invite|error|data|var|verifyInviteCode|makeInviteCode|how|to|generate|verify'.split('|'), 0, {}))

#### Eval

Evaluates or executes an argument, e.g. here is it executing (function(p,a,c,k,e,d)...)

#### Function

The function in question is p a c k e d.



#### Regex

Think of the forward slash as quotation marks for regular expressions. 
The slashes contain the expression but are not themselves part of the expression. 
(If you want to test for a forward slash, you have to escape it with a 
backwards slash.) The lowercase g specifies that this is a global search, i.e., 
find all matches rather than stopping at the first match.

So...

    {p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}
    
means...

While \b is 'word boundary' - Might not be applicable here.

'g' here is most likely the 'global' flag, which will 

    "Retain the index of the last match, allowing subsequent searches \
    to start from the end of the previous match. Without the global flag, \
    subsequent searches will return the same match."
