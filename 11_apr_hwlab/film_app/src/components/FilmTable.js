import React, { useState } from 'react';
import ExternalLink from "../containers/ExternalLink";
import Film from "../containers/Film";
import FilmForm from '../containers/FilmForm';

const FilmTable = () => {
    const [films, setFilms] = useState([
        {
            id: 1,
            name: "Spider-Man: Into the Spider-Verse",
            url: "https://www.imdb.com/title/tt4633694/?ref_=rlm"
          },
          {
            id: 2,
            name: "Life Itself",
            url: "https://www.imdb.com/title/tt5989218/?ref_=rlm"
          },
          {
            id: 3,
            name: "Mary Queen of Scots",
            url: "https://www.imdb.com/title/tt2328900/?ref_=rlm"
          },
          {
            id: 4,
            name: "The Lego Movie 2: The Second Part", 
            url: "https://www.imdb.com/title/tt3513498/?ref_=rlm"
          },
          {
            id: 5,
            name: "Captain Marvel",
            url: "https://www.imdb.com/title/tt4154664/?ref_=rlm"
          }
])

const addFilm = film => {
    setFilms([...films, film])
}

    return ( 
        <>
            <h2>Upcoming Film Releases for UK</h2>
            <ul>
                {films.map((film) => 
                    <Film
                    name = {film.name} 
                    url = {film.url}
                    key = {film.id}
                    />
                )}
            </ul>
            <FilmForm onFilmSubmit={addFilm}/>
            <footer>
                    <ExternalLink/>
            </footer>
        </>
     );
}
 
export default FilmTable;