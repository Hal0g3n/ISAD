<template>
  <div class="MMSE">
    <h1 class="subheading grey--text">MMSE</h1>

    <v-container class=ma-5 v-if=!memory>
        <v-btn @click="click"/>
    </v-container>
    
    <v-container class=ma-5 v-if=memory>
        <span>Do you remember your sins?</span>
        <v-btn @click="()=>this.$emit('complete', 'CVFT')"/>
    </v-container>

  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
    data: () => ({
        memory: false
    }),

    methods: {
        click() {
            this.$emit("complete", "CDT");
            setTimeout(()=>this.memory = true, 2000);
        }
    }
});

</script>