<template>
  <div>
    <div class="header">
      <h1>Foodics PAY</h1>
    </div>
    <div class="sideBar">
      <ul>
        <li><router-link to="/">Customer Dashboard</router-link></li>
        <li><router-link to="/sama">Sama Dashboard</router-link></li>
        <li><router-link to="/operation">Operation Dashboard</router-link></li>
      </ul>
    </div>
    <div class="body">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return{

    }
  },
}
</script>

<style scoped>
.header{
  width:100%;
  height:85px;
  background:#5f27cd;
  padding:0;
  position:relative;
  z-index:1;
}

.header h1{
    margin: 0;
    font-size: 25px;
    margin-left: 21px;
    color: #FFF;
    padding-top: 20px;
}

.sideBar{
  width:20%;
  height:100%;
  position:fixed;
  background:#5f27cd;
  left:0;
  top:0;
  padding-top:85px
}
.sideBar ul{
  list-style:none;
  padding:0 11%
}
.sideBar ul li{
  margin-bottom:15px;
  cursor:pointer;
}
.sideBar ul li a{
  color:#FFF;
  font-weight:bold;
}

.body{
  width:80%;
  height:auto;
  min-height:200px;
  float:right;
  padding:0 2%
}
</style>