import { Box, useTheme, Typography } from "@mui/material";

const Main = () => {
  const theme = useTheme();
  return (
    <Box
      sx={{
        flexGrow: 1,
        marginTop: `${theme.primaryAppBar.height}px`,
        height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
        overflow: "hidden",
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

export default Main;
