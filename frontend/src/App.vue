<template>


    <div :style="backgroundDiv" class="bg">
        <router-view />
    </div>



</template>

<script>
export default {
    name: 'App',
    data() {

        return {

            backgroundDiv: {

                backgroundImage: 'url(' + require('./images/网站背景图.jpg') + ')',

                backgroundRepeat: 'no-repeat',
                // width : 200,
                // height : 300,
                backgroundSize: '100% 100%',
                // backgroundSize: '100%',
      
            }

        }

    }


}
</script>

<style>
#app {
    font-family: "Gill Sans", sans-serif;
    color:rgb(196, 212, 211);
    /* margin-left: 40px; */
    /* margin-right: 40px; */
}

.bg {
    z-index: -1;
    position: absolute;
    top: calc(0px + 0px);
    left: 0;
    width: 100%;
    height: calc(100% - 0px);
    transition: .25s;
}
</style>


<!--<template>-->
<!--<img alt="Vue logo" src="./assets/logo.png">-->
<!--<HelloWorld msg="Welcome to Your Vue.js App"/>-->
<!--</template>-->

<!--<script>-->

<!--import HelloWorld from './components/HelloWorld.vue'-->


<!--export default {-->
<!--name: 'App',-->
<!--components: {-->
<!--HelloWorld-->
<!--}-->
<!--}-->

<!--</script>-->

<!--<style>-->
<!--#app {-->
<!--font-family: Avenir, Helvetica, Arial, sans-serif;-->
<!-- -webkit-font-smoothing: antialiased;-->
<!-- -moz-osx-font-smoothing: grayscale;-->
<!--text-align: center;-->
<!--color: #2c3e50;-->
<!--margin-top: 60px;-->
<!--}-->
<!--</style>-->
