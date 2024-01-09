import { Box, CssBaseline } from "@mui/material";
import Main from "./templates/Main";
import PrimaryAppBar from "./templates/PrimaryAppBar";
import PrimaryDrawer from "./templates/PrimaryDrawer";
import SecondaryDrawer from "./templates/SecondaryDrawer";
const Home = () => {
  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <PrimaryAppBar />
      <PrimaryDrawer />
      <SecondaryDrawer />
      <Main />
    </Box>
  );
};

export default Home;
