import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'

Vue.config.productionTip = false

const regiones = [
  "XV Región de Arica y Parinacota",
  "I Región de Tarapacá",
  "II Región de Antofagasta",
  "III Región de Atacama",
  "IV Región de Coquimbo",
  "V Región de Valparaíso",
  "Región Metropolitana de Santiago",
  "VI Libertador Bernardo O'Higgins",
  "VII Región del Maule",
  "XVI Región de Ñuble",
  "VIII Región del Biobío",
  "IX Región de La Araucanía",
  "XIV Región de Los Ríos",
  "X Región de Los Lagos",
  "XI Región de Aisén de General Carlos Ibáñez del Campo",
  "XII Región de Magallanes y Antártica Chilena",
];
Vue.prototype.$listRegiones = regiones;
Vue.prototype.$regiones = {
  0: regiones[6],
  1: regiones[1],
  2: regiones[2],
  3: regiones[3],
  4: regiones[4],
  5: regiones[5],
  6: regiones[7],
  7: regiones[8],
  8: regiones[10],
  9: regiones[11],
  10: regiones[13],
  11: regiones[14],
  12: regiones[15],
  14: regiones[12],
  15: regiones[0],
  16: regiones[9],
};

const showInfo = (data) => {
  if (data) {
    let returnValue = "";
    for (const element of data) {
      returnValue += element.toString().toUpperCase();
    }
    return returnValue;
  }
  return "";
}
Vue.prototype.$showInfo = showInfo;
Vue.prototype.$showExcerpt = (excerpt) => {
  const maxLarge = 160;
  let returnValue = showInfo(excerpt);
  returnValue = returnValue.substr(0,maxLarge);
  returnValue += "...";
  return returnValue;
}
Vue.prototype.$firstName = (name) => {
  let returnValue = showInfo(name);
  return returnValue.split(" ")[0];
}

Vue.prototype.$castData = (data) => {
  let castedData = [];
  for (const result of data) {
    castedData.push(JSON.parse(result.replace(/'/g, '"')));
  }
  return castedData;
}

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
