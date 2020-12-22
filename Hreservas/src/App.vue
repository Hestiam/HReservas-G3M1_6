<template>
  <div id="app">
    <div class="header">
      <h1>HReservas Online</h1>
      <nav>
        <button v-on:click="init">Inicio</button>
        <button v-on:click="buscar_cli">Buscar Cliente</button>
        <button v-on:click="registrar_cli">Registar Cliente</button>
        <button v-on:click="reservar">Reservar</button>
        <button v-on:click="buscar_hab">Busqueda Habitacion</button>
      </nav>
    </div>
    <div class="main-component">
      <router-view></router-view>
    </div>
    <div class="footer">
      <h2>Hoteles Ficticios S.A</h2>
    </div>
  </div>
</template>
<script>
export default {
  name: "App",
  
  methods: {
    init: function () {
      if (this.$route.name != "Inicio") {
        this.$router.push({ name: "Inicio" });
        this.$router.go({ name: "Inicio" });
      }
    },
    reservar: function(){this.$router.push({ name: "nueva_reserva" });
    this.$router.go({ name: "nueva_reserva" });
    },
    buscar_hab: function(){this.$router.push({ name: "buscar_habitacion" });
    this.$router.go({ name: "buscar_habitacion" });
    },
    buscar_cli: function(){this.$router.push({ name: "busqueda_Cliente" });
    this.$router.go({ name: "busqueda_Cliente" });
    },
    registrar_cli: function(){this.$router.push({ name: "nuevo_cliente" });
    this.$router.go({ name: "nuevo_cliente" });
    },
  },
  
  
};
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
  background-color: #283747;
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
  background: #283747;
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
  background-color: #283747;
  color: #e5e7e9;
}
.footer h2 {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
