<template>

    <!-- <div class="glass-container"> -->
    <BlogHeader />
    <!-- </div> -->
    <!-- <BlogHeader /> -->
    <div class="container">
        <div class="row">
            <div class="glass-container">
                <div class="col-sm-4">
                    <h3>第一列</h3>
                    <p>1</p>
                    <p>具体内容</p>
                </div>
            </div>
            <tr></tr>
            <div class="glass-container">
                <div class="col-sm-4">
                    <h3>第二列</h3>
                    <p>2..</p>
                    <p>具体内容</p>
                </div>
            </div>

            <div class="glass-container">
                <div class="col-sm-4">
                    <h3>第三列</h3>
                    <p>3..</p>
                    <p>具体内容</p>
                </div>
            </div>


        </div>
    </div>
    <BlogFooter />

</template>

<script>

import BlogHeader from '@/components/BlogHeader.vue'
import BlogFooter from '@/components/BlogFooter.vue'
// import ArticleList from '@/components/ArticleList.vue'



export default {
    name: 'Index',
    components: { BlogHeader, BlogFooter }
}

</script>

<style>
.glass-container {
    /* width: 700px; */
    /* height: 375px; */
    /* color: white; */
    /* display: flex; */
    /* justify-content: center; */
    /* align-items: center; */
    /* gap: 20px; */
    border-radius: 62px;
    backdrop-filter: blur(7px);
    background-color: rgba(0, 191, 255, 0);
    box-shadow: rgba(0, 0, 0, 0.3) 2px 8px 8px;
    border: 0px rgba(255, 255, 255, 0.4) solid;
    border-bottom: 0px rgba(40, 40, 40, 0.35) solid;
    border-right: 0px rgba(40, 40, 40, 0.35) solid;
}
</style>