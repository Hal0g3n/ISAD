<template>
    <nav>
        <v-toolbar flat app>
            <v-app-bar-nav-icon class="grey--text" @click="drawer = !drawer"></v-app-bar-nav-icon>

            <v-toolbar-title class = 'text-uppercase grey--text'>
                <div>ISAD</div>
            </v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn>
                Sign Out
                <v-icon right>mdi-logout</v-icon>
            </v-btn>

        </v-toolbar>

        <v-navigation-drawer v-model='drawer' temporary app color=primary>
            <v-list>
                <!-- Lists all the items in the nav bar -->
                <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
                    
                    <!-- The Title of the Navigation Drawer -->
                    <v-icon class="white--text">{{ link.icon }}</v-icon>
                    <v-list-item-content>
                        <v-list-item-title class=white--text>{{link.text}}</v-list-item-title>
                    </v-list-item-content>


                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        
    </nav>
</template>

<script lang="ts">

import Vue from "vue";

export default Vue.extend({
    name: "Navbar",
    data: () => ({
        drawer: false,
        links: [
            { icon: 'mdi-view-dashboard', text: 'Dashboard', route: '/' },
            { icon: 'mdi-folder', text: 'My Projects', route: '/projects' },
            { icon: 'mdi-account', text: 'Team', route: '/team' },
        ]
    })
});

</script>