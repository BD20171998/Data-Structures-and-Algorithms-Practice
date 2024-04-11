-- Top 5 Artists
-- https://datalemur.com/questions/top-fans-rank

with cte as (
    select
        artist_name,

        DENSE_RANK() over (order by COUNT(artist_name) desc) as artist_rank
    from artists
    inner join songs
        on artists.artist_id = songs.artist_id
    inner join global_song_rank
        on songs.song_id = global_song_rank.song_id
    where global_song_rank.rank < 11
    group by artist_name
)

select * from cte where artist_rank < 6