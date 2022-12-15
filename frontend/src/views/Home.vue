<template>

    <BlogHeader />

    <ArticleList />
    <div class="hello">
        <button type="button" class="btn btn-primary">Primary</button>
        <button class="btn btn-primary">确定 </button>

        <button class="btn btn-success">使用 </button>
         
        <button class="btn btn-danger">注意 </button>
    </div>


    <BlogFooter />

</template>

<script>
import BlogHeader from '@/components/BlogHeader.vue'
import BlogFooter from '@/components/BlogFooter.vue'
import ArticleList from '@/components/ArticleList.vue'


export default {
    name: 'Home',
    components: { BlogHeader, BlogFooter, ArticleList }
}
</script>