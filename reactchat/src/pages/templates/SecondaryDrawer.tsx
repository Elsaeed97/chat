import { Box, Typography, useTheme } from "@mui/material";

const SecondaryDrawer = () => {
  const theme = useTheme();
  return (
    <Box
      sx={{
        minWidth: `${theme.secondaryDrawer.width}px`,
        height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
        mt: `${theme.primaryAppBar.height}px`,
        borderRight: `1px solid ${theme.palette.divider}`,
        display: { xs: "none", sm: "block" },
        overflow: "auto",
        backgroundColor: "lightgray",
      }}
    >
      {[...Array(50)].map((_, i) => (
        <Typography key={i} paragraph>
          {i + 1}
        </Typography>
      ))}
    </Box>
  );
};

export default SecondaryDrawer;
