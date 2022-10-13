using System;
using System.Collections.Generic;
using System.Text;

namespace OnlineRadioDatabase_04
{
    public class Song
    {
        private string songName;
        private string artistName;
        private int minutes;
        private int seconds;

        public Song(string songName, string artistName, int minutes, int seconds)
        {
            this.SongName = songName;
            this.ArtistName = artistName;
            this.Minutes = minutes;
            this.Seconds = seconds;
        }

        public string SongName
        {
            get
            {
                return songName;
            }
            set
            {
                if (value.Length < 3 || value.Length > 30)
                {
                    throw new ArgumentException("Song name should be between 3 and 30 symbols.");
                }
                songName = value;
            }
        }

        public string ArtistName
        {
            get
            {
                return artistName;
            }
            set
            {
                if (value.Length < 3 || value.Length > 20)
                {
                    throw new ArgumentException("Artist name should be between 3 and 20 symbols.");
                }
                artistName = value;
            }
        }

        public int Minutes
        {
            get
            {
                return minutes;
            }
            set
            {
                if (value < 0 || value > 14)
                {
                    throw new ArgumentException("Song minutes should be between 0 and 14.");
                }
                minutes = value;
            }
        }

        public int Seconds
        {
            get
            {
                return seconds;
            }
            set
            {
                if (value < 0 || value > 59)
                {
                    throw new ArgumentException("Song seconds should be between 0 and 59.");
                }
                seconds = value;
            }
        }

        public int CalculatingLength()
        {
            int timeMinutes = Minutes * 60;
            int timeSeconds = Seconds;
            int allTime = timeSeconds + timeMinutes;
            if (allTime < 0 || allTime > 899)
            {
                throw new ArgumentException("Invalid song length.");
            }

            return allTime;
        }
    }

    class InvalidSongException : Exception
    {
        public const string InvalidSongExceptionn = "Invalid song.";
    }

    class Start
    {
        static void Main(string[] args)
        {
            List<Song> songs = new List<Song>();

            try
            {
                int n = int.Parse(Console.ReadLine());
                for (int i = 0; i < n; i++)
                {
                    var input = Console.ReadLine().Split(new char[] { ';', ':' }).ToArray();
                    if (input.Length == 4)
                    {
                        string artistName=input[0];
                        string songName = input[1];
                        int minutes = int.Parse(input[2]);
                        int seconds = int.Parse(input[3]);

                        Song song = new Song(songName,artistName,minutes,seconds);
                        songs.Add(song);
                        Console.WriteLine("Song added :)");
                    }
                    else
                    {
                        throw new ArgumentException("Invalid song");
                    }

                }

            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }

            int allTimeSeconds=0;
            foreach(var song in songs)
            {
                allTimeSeconds += song.CalculatingLength();
            }
            TimeSpan time = TimeSpan.FromSeconds(allTimeSeconds);

            Console.WriteLine($"Songs added {songs.Count}");
            Console.WriteLine($"PlayList length {time.Hours}h, {time.Minutes}m, {time.Seconds}s ");
        }
    }
}