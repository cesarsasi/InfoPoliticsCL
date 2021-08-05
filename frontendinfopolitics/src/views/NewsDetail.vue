<template>
  <v-flex class="pa-4 box">
    <v-row class="pa-4">
      <v-col class="d-flex justify-left">
        <v-btn @click="$router.go(-1)">
          <v-icon>mdi-home</v-icon>
          Volver a la página principal
        </v-btn>
      </v-col>
    </v-row>
    <v-card v-if="!empty">
      <v-card-title>
        <h2 class="h2">{{ $showInfo(newDetail.title) }}</h2>
      </v-card-title>
      <v-card-text>
        <h2 class="body-1">{{ $showInfo(newDetail.excerpt) }}</h2>
      </v-card-text>
      <v-card-actions>
        <h2 class="body-2">Fecha: {{ $showInfo(newDetail.date) }}</h2>
        <h2 class="body-2 pl-10">Fuente: Ciper Chile</h2>
      </v-card-actions>
    </v-card>
    <v-card v-else>
      <v-card-title>
        <h2 class="h1 text-center">La noticia no fue encontrada.</h2>
      </v-card-title>
    </v-card>
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
export default {
  data() {
    return {
      empty: false,
      newDetail: [],
    };
  },
  created() {
    const newDetail = this.$route.params.newDetail;
    if (newDetail) {
      this.newDetail = newDetail;
    } else {
      this.empty = true;
    }
  },
};
</script>
