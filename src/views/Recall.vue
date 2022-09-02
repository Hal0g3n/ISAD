<template>
  <div class="Recall">
    <h1 class="subheading grey--text">Do you remember?</h1>
    
    <v-container class=my-5>
        <v-row>
            <div>What is the first number?</div><v-text-field/></v-row>
        <v-row>
            <div>What is the second number?</div><v-text-field/></v-row>
        <v-row>
            <div>What is the third number?</div><v-text-field/></v-row>
        <v-btn @click="()=>this.$emit('complete','CVFT')"/>
    </v-container>
  </div>
</template>
