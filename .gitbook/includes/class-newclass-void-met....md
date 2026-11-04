---
title: class newClass {   void met...
---

<pre class="language-jsonp" data-overflow="wrap"><code class="lang-jsonp">class newClass {
   void method1(){
     for (int i = 0; i &#x3C; 10; i++){
<strong>       insert new Account(name = ‘Name ’ + i); //NOSONAR
</strong>     }
   }
}
</code></pre>
