<template>
  <div id="app">
    <div class="header">
      <h1>H-Reservas</h1>
      <nav>
        <button v-on:click="init">Inicio</button>
        <button v-on:click="nueva_Reserva">Reservar</button>
        <button v-on:click="busqueda_Cliente">Información Cliente</button>
      </nav>
    </div>
    <div class="main-component"></div>
    <div class="footer">
      <h2 align="center">Hotel Ficticio S.A.S</h2>
    </div>
    <div class="main-component">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
  data: {}
};
methods: {
  init: function(){
  if(this.$route.name != "cliente"){
  let nombre = localStorage.getItem("current_username")
  this.$router.push({name: "user", params:{username:username}})
}
}
</script>

<style>
body {
  margin: 0 0 0 0;
}
.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #1a6e4e;
  color: #e5e7e9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header h1 {
  width: 20%;
  text-align: center;
}
.header nav {
  height: 100%;
  width: 45%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}
.header nav button {
  color: #e5e7e9;
  background: #328f82;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 20px;
}
.header nav button:hover {
  color: #283747;
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
}
.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;
  background: #fdfefe;
}
.footer {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #1a6e4e;
  color: #e5e7e9;
}
footer h2 {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
