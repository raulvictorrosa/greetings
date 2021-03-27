import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import CssBaseline from '@material-ui/core/CssBaseline';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import axios from 'axios';
import React, { useEffect, useState } from 'react';

const useStyles = makeStyles(theme => ({
  paper: {
    paddingTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export default function App() {
  const [bkgColor, setBkgColor] = useState(null);
  const [greeting, setGreeting] = useState(null);

  const updateGreeting = async () => {
    const { data: greet } = await axios.get(`//localhost:8000/saudacao`);
    setGreeting(greet.message);
    setBkgColor(greet.color);
  };

  useEffect(() => {
    updateGreeting();
  }, []);

  const classes = useStyles();

  return (
    <div
      style={{
        display: 'block',
        backgroundColor: bkgColor,
        height: '100vh',
      }}
    >
      <Container component='main' maxWidth='xs'>
        <CssBaseline />
        <div className={classes.paper}>
          <Typography component='h1' variant='h5'>
            {greeting}
          </Typography>
          <Button
            type='submit'
            fullWidth
            variant='contained'
            color='primary'
            className={classes.submit}
            onClick={updateGreeting}
          >
            Atualizar
          </Button>
        </div>
      </Container>
    </div>
  );
}
