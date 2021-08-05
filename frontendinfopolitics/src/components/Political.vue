<template>
  <v-flex class="pa-4 d-flex justify-center">
    <v-card
      class="blue-grey lighten-5 text-left"
      min-width="85%"
      max-width="85%"
    >
      <v-row>
        <v-col cols="3">
          <img class="pl-8 pt-2" src="../../public/user.png" />
        </v-col>
        <v-col>
          <h1 class="font-weight-bold headline">
            {{ $showInfo(political.nombre) }}
          </h1>
          <h2 class="subtitle-1">Region: {{ $regiones[political.region] }}</h2>
          <h2 class="body-2">Comuna: {{ $showInfo(political.comuna) }}</h2>
          <h2 class="body-2">Partido: {{ $showInfo(political.partido) }}</h2>
        </v-col>
        <v-col align-self="center">
          <h2 class="subtitle-1 text-center">Cantidad de noticias</h2>
          <h2 class="text-center">{{countNews}}</h2>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="d-flex justify-center">
          <v-btn @click="goToNews">Noticias de {{$firstName(political.nombre)}}</v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-flex>
</template>
<script>
import axios from "axios";
export default {
  props: {
    political: {
      type: Object,
      default: () => {},
    },
  },
  data(){
    return{
      countNews: 0,
    }
  },
  created(){
    axios.get('http://localhost:4000/search/news/' + this.political.nombre + '/count_news').then(r => {
      this.countNews = r.data;
      //console.log("cantidad: ", this.countNews);
    }).catch(e => {
      console.log(e);
    });
  },
  methods:{
    goToNews: function (){
      this.$router.push({name: "New", params:{politicalName: this.political.nombre}});
    },
  },
};
</script>
