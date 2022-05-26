---
layout: default
---
<div class="home">

  <h1 class="page-heading">Latest analysis</h1>
  <ul class="post-list">
    {% for post in site.posts limit:1 %}
      {{ post.content }}
    {% endfor %}
    
  </ul>
</div>
