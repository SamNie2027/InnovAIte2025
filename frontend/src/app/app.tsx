import { SafeAreaView, StyleSheet } from "react-native";
import { TattleTell } from "../components/TattleTell";

export const App = () => {
  return (
    <SafeAreaView style={styles.safeArea}>
      <TattleTell />
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
