import { Drawer, useMediaQuery, useTheme } from "@mui/material";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
// import Typography from '@mui/material/Typography';
import MenuIcon from "@mui/icons-material/Menu";
import { Link, Typography } from "@mui/material";
import IconButton from "@mui/material/IconButton";
import { useEffect, useState } from "react";
const PrimaryAppBar = () => {
  const [sideMenu, setSideMenu] = useState(false);
  const theme = useTheme();
  const isSmallScreen = useMediaQuery(theme.breakpoints.up("sm"));

  useEffect(() => {
    if (isSmallScreen && sideMenu) {
      setSideMenu(false);
    }
  }, [isSmallScreen]);
  const toggleDrawer = (open: boolean) => (event: React.MouseEvent) => {
    setSideMenu(open);
  };
  return (
    <Box sx={{ position: "flex" }}>
      <AppBar
        position="static"
        sx={{
          // position: 'fixed', boxSizing: 'border-box',
          backgroundColor: theme.palette.background.default,
          // borderBottom: `1px solid ${theme.palette.divider}`,
        }}
      >
        <Toolbar
          sx={{
            zIndex: (theme) => theme.zIndex.drawer + 2,
            height: theme.primaryAppBar.height,
            minHeight: theme.primaryAppBar.height,
          }}
        >
          <Box sx={{ display: { xs: "block", sm: "none" } }}>
            <IconButton
              size="large"
              edge="start"
              onClick={toggleDrawer(true)}
              color="inherit"
              aria-label="open drawer"
              sx={{ mr: 2 }}
            >
              <MenuIcon />
            </IconButton>
          </Box>
          <Drawer anchor="left" open={sideMenu} onClose={toggleDrawer(false)}>
            {[...Array(20)].map((_, i) => (
              <Typography key={i} paragraph>
                {i + 1}
              </Typography>
            ))}
          </Drawer>
          <Typography
            variant="h6"
            component="div"
            noWrap
            sx={{
              flexGrow: 1,
              display: { fontWeight: 700, letterSpacing: "-0.5px" },
            }}
          >
            <Link underline="none" color="inherit" href="/">
              DJChat
            </Link>
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default PrimaryAppBar;
