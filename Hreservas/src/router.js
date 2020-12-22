import vueRouter from 'vue-router'
import Cliente from './components/Cliente'
import Reserva from './components/Reservas'
import Inicio from './components/Inicio'
import Habitacion_busqueda from './components/Habitacion_busqueda'
import Cliente_busqueda from './components/Cliente_busqueda'
import App from './App'

const router = new vueRouter({
    mode: 'history',
    base: __dirname,
    routes: [
        {
            path: '/',
            name: "root",
            component: Inicio
        },
        {
            path: '/Inicio/',
            name: "Inicio",
            component: Inicio
        },
        {
            path: '/Cliente/buscar',
            name: "busqueda_Cliente",
            component: Cliente_busqueda
        },
        {
            path: '/Cliente/registrar/',
            name: "nuevo_cliente",
            component: Cliente
        },
        {
            path: '/Reserva/reservar/',
            name: "nueva_reserva",
            component: Reserva
        },
        {
            path: '/Habitacion/buscar/',
            name: "buscar_habitacion",
            component: Habitacion_busqueda
        },
        

    ]
})
export default router