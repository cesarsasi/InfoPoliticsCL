<template>
  <v-flex class="pa-16 px-16 box">
    <v-row>
      <v-col class="d-flex justify-start">
        <v-btn href="/">
          <v-icon>mdi-arrow-left</v-icon>
          Volver al inicio
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="d-flex justify-center">
        <v-card>
          <h1 v-if="hasName" class="text-center px-4">Noticias de {{$showInfo(hasName)}}</h1>
          <h1 v-else class="text-center px-4">Noticias</h1>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="6" v-for="(notice, index) in news" :key="index">
        <News :notice="notice"></News>
      </v-col>
    </v-row>
  </v-flex>
</template>
<style>
.box {
  background: url("../../public/newspaper.jpg") fixed;
  background-size: cover;
  height: 100%;
}
</style>
<script>
import News from "@/components/News.vue";
import axios from "axios";
export default {
  components: {
    News,
  },
  data() {
    return {
      news: [],
      hasName: undefined,
    };
  },
  created() {
    const politicalName = this.$route.params.politicalName;
    if (politicalName) {
      this.hasName = politicalName;
      axios.get("http://localhost:4000/search/news/" + politicalName).then(r => {
        this.news = this.$castData(r.data);
        console.log("Casted data: ", r.data);
      }).catch(e => {
        console.log(e);
      });
    } else {
      axios
        .get("http://localhost:4000/search/news")
        .then((r) => {
          this.news = this.$castData(r.data);
          console.log("Casted data: ", this.news);
        })
        .catch((e) => {
          console.log(e);
        });
    }
  },
};
</script>
