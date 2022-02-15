<template>
  <div id="app">
      <AdminLayout />
  </div>
</template>

<script>
import Vue from "vue";

import AdminLayout from '@/views/adminRoutes/AdminLayout'

export default Vue.extend({
  name: "app",

  components: {
    AdminLayout
  },
  data() {
    return {
    };
  },

});
</script>
<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Open+Sans&display=swap");
@import url('https://fonts.googleapis.com/css?family=Cairo&display=swap');
// @import 'node_modules/bootstrap/scss/bootstrap.scss';
// @import 'node_modules/bootstrap-vue/src/index.scss';


:root {
  --main-color: rgba(255, 117, 0, 1);
  --second-color: rgba(5, 199, 242, 1);
  --black: #000;
  --white: #fff;
  --background-color: rgba(241, 243, 255, 1);
  --light-gray: rgba(158, 158, 158, 1);
  --dark-gray: rgba(120, 120, 120, 1);
  --normal-shadow: 1px 1px 5px 1px rgba(0, 0, 0, 0.13);
  --high-shadow: 5px 7px 5px 0px rgba(0, 0, 0, 0.13);
  --lw-radius: 7px;
  --md-radius: 15px;
  --lg-radius: 25px;
}

html,
body,
#app,
#app > div {
  // height: 100%;
}
* {
  box-sizing: border-box;
  font-family: "Open Sans" ,"Cairo", sans-serif;
  text-decoration: none !important;
  outline: none;
  outline-color: none;
  outline-offset: none;
}

body {
  margin: 0;
  background: var(--background-color);
}

#app {
  background: var(--background-color);
}

.container {
  width: 95%;
  height: auto;
  margin: auto;
}
@font-face {
  font-family: "MV Boli";
  src: url("./assets/fonts/mvboli.ttf");
}

/******************** Start  Responsive Website ***********************/
@media (max-width:359px) and (min-width:0){

}

/******************** End Screen max-width:319px **************************/    










/******************** Start Screen max-width:459px **************************/    
@media( max-width : 459px ) and ( min-width : 360px){ 

}
/******************** End Screen max-width:459px **************************/    










/******************** Start Screen max-width:559px **************************/    
@media ( max-width : 559px ) and ( min-width : 460px) {

}
/******************** End Screen max-width:559px **************************/    












/******************** Start Screen max-width:639px **************************/    
@media ( max-width : 639px ) and ( min-width : 560px) {

}
/******************** End Screen max-width:639px **************************/    










/******************** Start Screen max-width:719px **************************/    
@media ( max-width : 719px ) and ( min-width : 640px) {

}
/******************** End Screen max-width:719px **************************/










/******************** Start Screen max-width:959px **************************/
@media ( max-width : 959px ) and ( min-width : 720px) {

}
/******************** End Screen max-width:959px **************************/






/******************** Start Screen max-width:1023px **************************/
@media ( max-width : 1023px ) and ( min-width : 960px) {
    
}
/******************** End Screen max-width:1023px **************************/










/******************** Start Screen max-width:1160px **************************/
@media ( max-width : 1160px ) and ( min-width : 1024px) {

}
/******************** End Screen max-width:1160px **************************/






/******************** Start Screen max-width:1199px **************************/
@media only screen and ( max-width : 1199px ) and ( min-width : 1161px) { 
  .container{
    width: 98%;
  }    
}
/******************** End Screen max-width:1199px **************************/
</style>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

