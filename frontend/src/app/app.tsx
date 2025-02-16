import { SafeAreaView, StyleSheet } from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { TattleTell } from "../components/TattleTell";
import { Camera } from "../components/Camera";
import React from "react";

type RootStackParamList = {
  Main: undefined;
  Camera: undefined;
};

const RootStack = createNativeStackNavigator<RootStackParamList>();

const Navigation = () => (
  <NavigationContainer>
    <RootStack.Navigator initialRouteName="Main">
      <RootStack.Screen name="Main" component={TattleTell} />
      <RootStack.Screen name="Camera" component={Camera} />
    </RootStack.Navigator>
  </NavigationContainer>
);

export const App = () => {
  return (
    <SafeAreaView style={styles.safeArea}>
      <Navigation />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: "#79B791",
  },
});

export default App;